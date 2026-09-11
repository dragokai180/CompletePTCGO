from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='62a287a7-6626-5f4d-aeba-87a411688eda',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LugiaGX.Name',
    display_name='Lugia-GX',
    searchable_by=['Lugia-GX', 'Basic', 'GX', 'LugiaGX'],
    subtypes=['Basic', 'GX'],
    collector_number=159,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Attack(
            title='Psychic',
            game_text="This attack does 30 more damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Pelagic Blade',
            game_text="This Pokémon can't use Pelagic Blade during your next turn.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=170,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Lost Purge-GX',
            game_text="Put your opponent's Active Pokémon and all cards attached to it in the Lost Zone. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
