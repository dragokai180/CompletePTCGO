from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d4f910e-d823-5a9e-849e-7de8a0458e8e',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaGX.Name',
    display_name='Greninja-GX',
    searchable_by=['Greninja-GX', 'Stage 2', 'GX', 'GreninjaGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=24,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    family_id=656,
    abilities=[
        Ability(
            title='Shuriken Flurry',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put 3 damage counters on 1 of your opponent's Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Haze Slash',
            game_text='You may shuffle this Pokémon and all cards attached to it into your deck.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=standard_attack,
        ),
        Attack(
            title='Shadowy Hunter-GX',
            game_text="This attack does 130 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
