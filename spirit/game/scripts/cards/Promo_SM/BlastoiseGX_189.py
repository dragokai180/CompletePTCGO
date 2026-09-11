from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4a373b2-155e-506b-bfd1-42dfe2f74982',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseGX.Name',
    display_name='Blastoise-GX',
    searchable_by=['Blastoise-GX', 'Stage 2', 'GX', 'BlastoiseGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=189,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name',
    family_id=9,
    abilities=[
        Ability(
            title='Solid Shell',
            game_text='This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Rocket Splash',
            game_text='Shuffle any amount of Water Energy from your Pokémon into your deck. This attack does 60 damage for each card you shuffled into your deck in this way.',
            cost={PokemonTypes.WATER: 2},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Giant Geyser-GX',
            game_text="Attach any number of Water Energy cards from your hand to your Pokémon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
