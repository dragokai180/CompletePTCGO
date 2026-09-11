from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='997a24ad-3af5-52be-aa84-d2e8930b7d07',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.NecrozmaGX.Name',
    display_name='Necrozma-GX',
    searchable_by=['Necrozma-GX', 'Basic', 'GX', 'NecrozmaGX'],
    subtypes=['Basic', 'GX'],
    collector_number=58,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=800,
    abilities=[
        Ability(
            title="Light's End",
            game_text='Prevent all damage done to this Pokémon by attacks from Colorless Pokémon.',
            passive=standard_passive('Prevent all damage done to this Pokémon by attacks from Colorless Pokémon.'),
        ),
        Attack(
            title='Prismatic Burst',
            game_text='Discard all Psychic Energy from this Pokémon. This attack does 60 more damage for each card you discarded in this way.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Black Ray-GX',
            game_text="This attack does 100 damage to each of your opponent's Pokémon-GX and Pokémon-EX. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
