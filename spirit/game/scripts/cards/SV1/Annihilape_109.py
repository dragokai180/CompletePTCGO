from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eecbda55-8a8e-51d4-8b4f-9fff9e6e13fd',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Annihilape.Name',
    display_name='Annihilape',
    searchable_by=['Annihilape', 'Stage 2', 'Annihilape'],
    subtypes=['Stage 2'],
    collector_number=109,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name',
    family_id=56,
    abilities=[
        Attack(
            title='Rage Fist',
            game_text='This attack does 70 damage for each Prize card your opponent has taken.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Dynamite Punch',
            game_text='This Pokémon also does 50 damage to itself.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
