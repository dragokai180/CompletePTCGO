from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a441ee67-e721-53bd-a96a-fa4b9dd7aad0',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name',
    display_name='Girafarig',
    searchable_by=['Girafarig', 'Basic', 'Girafarig'],
    subtypes=['Basic'],
    collector_number=154,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=203,
    abilities=[
        Attack(
            title='Psy Bolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Headbang',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
