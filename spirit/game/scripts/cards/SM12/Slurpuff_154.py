from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c5fd3e8e-64a6-5483-a756-2924be50abf7',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name',
    display_name='Slurpuff',
    searchable_by=['Slurpuff', 'Stage 1', 'Slurpuff'],
    subtypes=['Stage 1'],
    collector_number=154,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name',
    family_id=684,
    abilities=[
        Attack(
            title='Olfactory Enchantment',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sweet Panic',
            game_text="If your opponent's Active Pokémon isn't Confused, this attack does nothing.",
            cost={PokemonTypes.FAIRY: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
