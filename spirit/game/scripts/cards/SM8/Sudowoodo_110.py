from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='def1a34e-9025-584c-8432-7b366ca67c9f',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name',
    display_name='Sudowoodo',
    searchable_by=['Sudowoodo', 'Basic', 'Sudowoodo'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=185,
    abilities=[
        Attack(
            title='Reply Strongly',
            game_text="If this Pokémon was damaged by an attack during your opponent's last turn while it was your Active Pokémon, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
