from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3ecad8f6-bf70-56a0-a7bf-59edc2955c20',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name',
    display_name='Alolan Vulpix',
    searchable_by=['Alolan Vulpix', 'Basic', 'AlolanVulpix'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=37,
    abilities=[
        Attack(
            title='Powder Snow',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Asleep.",
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Icy Snow',
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
