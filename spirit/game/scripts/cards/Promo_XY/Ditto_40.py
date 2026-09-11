from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad9d7205-fd76-5fda-80c2-6f9cddae0abe',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name',
    display_name='Ditto',
    searchable_by=['Ditto', 'Basic', 'Ditto'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=132,
    abilities=[
        Ability(
            title='Metamorphosis Gene',
            game_text="If this Pokémon is your Active Pokémon, it can use the attacks of your opponent's Active Pokémon. (You still need the necessary Energy to use each attack.)",
            passive=standard_passive("If this Pokémon is your Active Pokémon, it can use the attacks of your opponent's Active Pokémon. (You still need the necessary Energy to use each attack.)"),
        ),
        Attack(
            title='Stick On',
            game_text='Attach a basic Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
