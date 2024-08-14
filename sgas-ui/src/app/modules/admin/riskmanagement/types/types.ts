export interface Department {
    id: number;
    name: string;
    description: string;
  }

// TypeScript Enums for Django TextChoices

export enum Duration {
  CURTO_PRAZO = 'Curto Prazo',
  MEDIO_PRAZO = 'Médio Prazo',
  LONGO_PRAZO = 'Longo Prazo'
}


export enum Extension {
  LOCAL = 'Local',
  REGIONAL = 'Regional',
  NACIONAL = 'Nacional',
  GLOBAL = 'Global'
}

export enum Intensity {
  BAIXA = 'Baixa',
  MEDIA = 'Média',
  ALTA = 'Alta'
}

export enum LifeCycle {
  PRE_CONSTRUCAO = 'Pré-Construção',
  CONSTRUCAO = 'Construção',
  OPERACAO = 'Operação',
  DESATIVACAO = 'Desativação',
  ENCERRAMENTO = 'Encerramento',
  REINTEGRACAO_RESTAURACAO = 'Reintegração/Restauração'
}

export enum Probability {
  IMPROVAVEL = 'Improvável',
  PROVAVEL = 'Provável',
  ALTAMENTE_PROVAVEL = 'Altamente Provável',
  DEFINITIVA = 'Definitiva'
}

export enum ResponseType {
  SIM = 'Sim',
  NAO = 'Não'
}

export enum Statute {
  POSITIVO = 'Positivo',
  NEGATIVO = 'Negativo'
}
