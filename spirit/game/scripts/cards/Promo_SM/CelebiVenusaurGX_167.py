from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f7c1046d-f967-5210-bb10-79b3f875da0b',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CelebiVenusaurGX.Name',
    display_name='Celebi & Venusaur-GX',
    searchable_by=['Celebi & Venusaur-GX', 'Basic', 'TAG TEAM', 'GX', 'CelebiVenusaurGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=167,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=3,
    abilities=[
        Attack(
            title='Pollen Hazard',
            game_text="Your opponent's Active Pokémon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
        ),
        Attack(
            title='Evergreen-GX',
            game_text="Heal all damage from this Pokémon. If this Pokémon has at least 1 extra Grass Energy attached to it (in addition to this attack's cost), shuffle all cards from your discard pile into your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
