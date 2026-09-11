from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b73c1ac-823d-5757-9802-23c78efd05a7',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name',
    display_name='Suicune',
    searchable_by=['Suicune', 'Basic', 'Suicune'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=245,
    abilities=[
        Ability(
            title='Frozen Flow',
            game_text='Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may have your opponent switch their Active Pokémon with 1 of their Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Aurora Gain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
