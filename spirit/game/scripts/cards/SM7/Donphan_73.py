from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='453667a2-65e5-5f80-b9b4-77d6e6f90e5a',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name',
    display_name='Donphan',
    searchable_by=['Donphan', 'Stage 1', 'Donphan'],
    subtypes=['Stage 1'],
    collector_number=73,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    family_id=231,
    abilities=[
        Attack(
            title='Flail',
            game_text='This attack does 10 damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Rapid Spin',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon. If you do, your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
