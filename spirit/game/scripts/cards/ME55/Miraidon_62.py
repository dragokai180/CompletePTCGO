from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b324b20e-8650-564c-90c5-37627f2687f8',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name',
    display_name='Miraidon',
    searchable_by=['Miraidon', 'Basic', 'Miraidon'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=1008,
    abilities=[
        Attack(
            title='Mach Bolt',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title='Electro Drift',
            game_text='Discard 2 Lightning Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
