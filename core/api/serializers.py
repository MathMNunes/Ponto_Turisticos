from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from core.models import PontoTuristico, DocIdentificacao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco

class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer (ModelSerializer):
    atracoes = AtracaoSerializer(many = True)
    endereco = EnderecoSerializer(read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    doc_identificacao = DocIdentificacaoSerializer()
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao','aprovado', 'foto',
              'atracoes', 'comentarios','avaliacoes','endereco'
                ,'descricao_completa', 'descricao_completa2','doc_identificacao'   )
        
        read_only_fields = ('comentarios', 'avaliacoes')


    #Aqui esta sendo criado o ponto e criando junto as atraçoes ai por ser ManytoMany 
    #Sendo assim cria duas funções para contruir o ponto e outro a atração.
    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)


    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci
        
        ponto.save()

        return ponto


    def get_descricao_completa(self, obj):
        return '%s -- %s' % (obj.nome, obj.descricao)