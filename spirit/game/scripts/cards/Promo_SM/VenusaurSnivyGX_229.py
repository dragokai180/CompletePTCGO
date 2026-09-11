from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7d1166c-3630-5ca9-8770-8eec68c5d4f2',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurSnivyGX.Name',
    display_name='Venusaur & Snivy-GX',
    searchable_by=['Venusaur & Snivy-GX', 'Basic', 'TAG TEAM', 'GX', 'VenusaurSnivyGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=229,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=3,
    abilities=[
        Ability(
            title='Shining Vine',
            game_text="Once during your turn, if this Pokémon is your Active Pokémon, when you attach a Grass Energy card from your hand to it, you may switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Forest Dump',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
        Attack(
            title='Solar Plant-GX',
            game_text="This attack does 50 damage to each of your opponent's Pokémon. If this Pokémon has at least 2 extra Energy attached to it (in addition to this attack's cost), heal all damage from all of your Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
