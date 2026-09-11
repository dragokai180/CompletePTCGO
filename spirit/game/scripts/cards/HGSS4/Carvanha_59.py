from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='05fbb793-ba0c-5f56-a603-47c790ccbd05',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name',
    display_name='Carvanha',
    searchable_by=['Carvanha', 'Basic', 'Carvanha'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=318,
    abilities=[
        Attack(
            title='Focus Energy',
            game_text="During your next turn, Carvanha's Bite attack's base damage is 40.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
