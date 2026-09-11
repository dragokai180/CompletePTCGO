from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='245b3323-a1bd-5ad1-ade4-3381f325dd14',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name',
    display_name='Aromatisse',
    searchable_by=['Aromatisse', 'Stage 1', 'Aromatisse'],
    subtypes=['Stage 1'],
    collector_number=85,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name',
    family_id=682,
    abilities=[
        Attack(
            title='Dizzying Cologne',
            game_text="If your opponent's Active Pokémon is a Pokémon-EX, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
