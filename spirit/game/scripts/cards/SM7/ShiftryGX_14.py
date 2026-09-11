from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b2506ec-8762-5b41-a228-6447a18a4bed',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShiftryGX.Name',
    display_name='Shiftry-GX',
    searchable_by=['Shiftry-GX', 'Stage 2', 'GX', 'ShiftryGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=14,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name',
    family_id=273,
    abilities=[
        Attack(
            title='Perplex',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Extrasensory',
            game_text='If you have the same number of cards in your hand as your opponent, this attack does 90 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Den of Iniquity-GX',
            game_text="Choose 1 of your opponent's Pokémon. Your opponent shuffles that Pokémon and all cards attached to it into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
