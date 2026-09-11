from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3cd923f5-73c1-57db-869e-e52c094162ef',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteGX.Name',
    display_name='Dragonite-GX',
    searchable_by=['Dragonite-GX', 'Stage 2', 'GX', 'DragoniteGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=156,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    family_id=149,
    abilities=[
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=70,
        ),
        Attack(
            title='Giga Impact',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=standard_attack,
        ),
        Attack(
            title='Dragonporter-GX',
            game_text="Put 3 Dragon Pokémon from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
