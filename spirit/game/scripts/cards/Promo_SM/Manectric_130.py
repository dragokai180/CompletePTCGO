from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c8471fcc-7d43-5ef5-92c0-7576dd85f850',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name',
    display_name='Manectric',
    searchable_by=['Manectric', 'Stage 1', 'Manectric'],
    subtypes=['Stage 1'],
    collector_number=130,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name',
    family_id=310,
    abilities=[
        Ability(
            title='Electric Start',
            game_text='If you go second, and if this Pokémon is in your hand when you are setting up to play, you may put it face down as your Active Pokémon or on your Bench.',
            effect=standard_ability,
            usable_from='hand',
        ),
        Attack(
            title='Double Charge',
            game_text='You may attach up to 2 basic Energy cards from your hand to 1 of your Benched Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
