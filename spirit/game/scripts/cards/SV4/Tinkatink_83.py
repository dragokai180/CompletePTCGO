from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8237f51-afc7-54c0-8f8a-14d57ea8dea5',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name',
    display_name='Tinkatink',
    searchable_by=['Tinkatink', 'Basic', 'Tinkatink'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=957,
    abilities=[
        Attack(
            title='Boundless Power',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
