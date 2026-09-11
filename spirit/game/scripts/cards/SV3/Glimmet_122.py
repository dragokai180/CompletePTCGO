from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b64bb4d7-f96e-5403-a87e-52eb060f8bbf',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name',
    display_name='Glimmet',
    searchable_by=['Glimmet', 'Basic', 'Glimmet'],
    subtypes=['Basic'],
    collector_number=122,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=969,
    abilities=[
        Attack(
            title='Poison Shard',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
