from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4b517a3-2b29-5dc0-ab72-4dbbe747d561',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name',
    display_name='Mawile',
    searchable_by=['Mawile', 'Basic', 'Mawile'],
    subtypes=['Basic'],
    collector_number=91,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=303,
    abilities=[
        Attack(
            title='Mining',
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck. If that card is a Pokémon Tool card, instead of putting it into your hand, you may attach it to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite Off',
            game_text="If your opponent's Active Pokémon is a Pokémon-GX or a Pokémon-EX, this attack does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
