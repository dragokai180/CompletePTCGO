from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f992c92b-170e-5311-85f1-f28341ce3c8b',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ScizorEX.Name',
    display_name='Scizor-EX',
    searchable_by=['Scizor-EX', 'Basic', 'EX', 'ScizorEX'],
    subtypes=['Basic', 'EX'],
    collector_number=76,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=212,
    abilities=[
        Attack(
            title='Steel Wing',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Gale Thrust',
            game_text='If this Pokémon was on the Bench and became your Active Pokémon this turn, this attack does 60 more damage.',
            cost={PokemonTypes.METAL: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
