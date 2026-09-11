from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3b67b090-5e26-51f4-831c-903cf259bad5',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Emolga.Name',
    display_name='Emolga',
    searchable_by=['Emolga', 'Basic', 'Emolga'],
    subtypes=['Basic'],
    collector_number=35,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=587,
    abilities=[
        Attack(
            title='Energy Catch',
            game_text='Put 3 basic Energy cards from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Volt Switch',
            game_text='Switch this Pokémon with 1 of your Benched Lightning Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
