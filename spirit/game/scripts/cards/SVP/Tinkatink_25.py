from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='29a2ec25-87d1-5bc8-bb8e-8b15b3d0e17b',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name',
    display_name='Tinkatink',
    searchable_by=['Tinkatink', 'Basic', 'Tinkatink'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=957,
    abilities=[
        Attack(
            title='Smithereen Smash',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
