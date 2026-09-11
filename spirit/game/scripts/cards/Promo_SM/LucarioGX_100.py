from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3166d3f4-2fab-569d-b588-38eb5aa5455a',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LucarioGX.Name',
    display_name='Lucario-GX',
    searchable_by=['Lucario-GX', 'Stage 1', 'GX', 'LucarioGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=100,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    family_id=448,
    abilities=[
        Attack(
            title='Aura Strike',
            game_text='If this Pokémon evolved from Riolu during this turn, this attack does 90 more damage.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Cyclone Kick',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
        Attack(
            title='Cantankerous Beatdown-GX',
            game_text="This attack does 30 damage for each damage counter on this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
