from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e05a32cd-0060-560b-a9c1-81b8f736b66c',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShiningHoOh.Name',
    display_name='Shining Ho-Oh',
    searchable_by=['Shining Ho-Oh', 'Basic', 'ShiningHoOh'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title='Golden Wing',
            game_text="If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, move up to 2 basic Energy cards from this Pokémon to your Benched Pokémon in any way you like.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, move up to 2 basic Energy cards from this Pokémon to your Benched Pokémon in any way you like."),
        ),
        Attack(
            title='Fire Blast',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
