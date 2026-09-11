from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cdd72a99-c6a6-5090-8c09-956e450484c2',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name',
    display_name='Bagon',
    searchable_by=['Bagon', 'Basic', 'Bagon'],
    subtypes=['Basic'],
    collector_number=103,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=371,
    abilities=[
        Attack(
            title='Rock Head',
            game_text="During your opponent's next turn, this Pokémon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
