from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='04537340-f398-5375-b4f8-0d6cecb36fd9',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    display_name='Meowth',
    searchable_by=['Meowth', 'Basic', 'Meowth'],
    subtypes=['Basic'],
    collector_number=101,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=52,
    abilities=[
        Attack(
            title='Fake Out',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
