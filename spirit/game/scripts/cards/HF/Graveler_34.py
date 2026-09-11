from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1b606ec8-2a82-518f-8174-6964791d6c79',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name',
    display_name='Graveler',
    searchable_by=['Graveler', 'Stage 1', 'Graveler'],
    subtypes=['Stage 1'],
    collector_number=34,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Mudslide',
            game_text="Discard 2 Fighting Energy from this Pokémon. This attack does 80 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
