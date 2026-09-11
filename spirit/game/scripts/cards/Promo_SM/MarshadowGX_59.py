from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='642dfe81-6a0b-52e2-a9b4-eb392c885693',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MarshadowGX.Name',
    display_name='Marshadow-GX',
    searchable_by=['Marshadow-GX', 'Basic', 'GX', 'MarshadowGX'],
    subtypes=['Basic', 'GX'],
    collector_number=59,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=802,
    abilities=[
        Ability(
            title='Shadow Hunt',
            game_text='This Pokémon can use the attacks of Basic Pokémon in your discard pile. (You still need the necessary Energy to use each attack.)',
            effect=standard_ability,
            usable_from='discard',
        ),
        Attack(
            title='Beatdown',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title='Peerless Hundred Blows-GX',
            game_text="This attack does 50 damage times the number of basic Energy attached to this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
