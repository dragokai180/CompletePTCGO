from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2bf0ee15-ca6d-5c93-ae7a-746c64199ca2',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name',
    display_name='Wobbuffet',
    searchable_by=['Wobbuffet', 'Basic', 'Wobbuffet'],
    subtypes=['Basic'],
    collector_number=93,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=202,
    abilities=[
        Ability(
            title='Shady Tail',
            game_text="As long as this Pokémon is on your Bench, ◇ (Prism Star) Pokémon in play (both yours and your opponent's) can't attack and have no Abilities.",
            passive=standard_passive("As long as this Pokémon is on your Bench, ◇ (Prism Star) Pokémon in play (both yours and your opponent's) can't attack and have no Abilities."),
        ),
        Attack(
            title='Knock Away',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
