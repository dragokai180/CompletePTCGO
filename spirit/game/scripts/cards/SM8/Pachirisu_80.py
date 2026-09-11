from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='74892912-98b3-568b-9657-45d363e77a82',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name',
    display_name='Pachirisu',
    searchable_by=['Pachirisu', 'Basic', 'Pachirisu'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=417,
    abilities=[
        Attack(
            title='Overshort',
            game_text="Before doing damage, discard all Pokémon Tool cards from your opponent's Active Pokémon. If you discarded a Pokémon Tool card in this way, this attack does 40 more damage, and your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
