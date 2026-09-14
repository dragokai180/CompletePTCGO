from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='465f1b22-be43-58f6-bb71-e5c734c4583b',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    display_name='Porygon2',
    searchable_by=['Porygon2', 'Stage 1', 'Porygon2'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name',
    family_id=137,
    abilities=[
        Ability(
            title='Mapping',
            game_text='Once during your turn, when you play Porygon2 from your hand to evolve 1 of your Pokémon, you may search your deck for a Stadium card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.',
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='3-D Attack',
            game_text='Flip 3 coins. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
