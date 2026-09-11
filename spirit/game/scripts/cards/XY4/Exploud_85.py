from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9c32cdda-9127-5a8e-85c7-5a631fea5790',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name',
    display_name='Exploud',
    searchable_by=['Exploud', 'Stage 2', 'Exploud'],
    subtypes=['Stage 2'],
    collector_number=85,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name',
    family_id=293,
    abilities=[
        Attack(
            title='Boomburst',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Hyper Voice',
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
        ),
    ],
)
