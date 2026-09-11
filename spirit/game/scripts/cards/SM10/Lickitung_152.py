from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e32fe0ec-fbcd-5768-9062-ff013df7ee8c',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name',
    display_name='Lickitung',
    searchable_by=['Lickitung', 'Basic', 'Lickitung'],
    subtypes=['Basic'],
    collector_number=152,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=108,
    abilities=[
        Attack(
            title='Lick',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
