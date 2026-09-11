from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='21801e35-e080-55bb-a28f-26ed45adc7cf',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name',
    display_name='Azelf',
    searchable_by=['Azelf', 'Basic', 'Azelf'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=482,
    abilities=[
        Attack(
            title='Psychic Abduction',
            game_text="You can use this attack only if you go second, and only on your first turn. Shuffle 1 of your opponent's Benched Pokémon and all cards attached to it into their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hypnoblast',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
