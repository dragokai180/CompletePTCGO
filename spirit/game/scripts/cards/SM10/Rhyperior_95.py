from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e7ad0cd1-6002-57e1-b350-8ec167f5c5ec',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name',
    display_name='Rhyperior',
    searchable_by=['Rhyperior', 'Stage 2', 'Rhyperior'],
    subtypes=['Stage 2'],
    collector_number=95,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name',
    family_id=111,
    abilities=[
        Attack(
            title='Hefty Cannon',
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title='Break Ground',
            game_text="This attack does 20 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
