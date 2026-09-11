from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10b9217c-fcec-5f3c-8db6-c4ce6e7ac44c',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonGX.Name',
    display_name='Vaporeon-GX',
    searchable_by=['Vaporeon-GX', 'Stage 1', 'GX', 'VaporeonGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=172,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Ability(
            title='Hydrating Drops',
            game_text='Once during your turn (before your attack), you may heal 30 damage from your Active Water Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hydro Pump',
            game_text='This attack does 30 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Cure Shower-GX',
            game_text="Heal all damage from all of your Water Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
