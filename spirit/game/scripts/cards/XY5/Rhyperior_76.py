from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f1571194-89da-5c69-b11e-5ee52651697a',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name',
    display_name='Rhyperior',
    searchable_by=['Rhyperior', 'Stage 2', 'Rhyperior'],
    subtypes=['Stage 2'],
    collector_number=76,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name',
    family_id=111,
    abilities=[
        Attack(
            title='Rock Shower',
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Stone Edge',
            game_text='Flip a coin. If heads, this attack does 40 more damage.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
