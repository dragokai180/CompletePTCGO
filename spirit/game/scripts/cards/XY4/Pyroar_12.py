from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='86b62ae9-c659-50e2-bd90-bb27f643b63b',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name',
    display_name='Pyroar',
    searchable_by=['Pyroar', 'Stage 1', 'Pyroar'],
    subtypes=['Stage 1'],
    collector_number=12,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    family_id=667,
    abilities=[
        Ability(
            title='Flare Command',
            game_text="Once during your turn (before your attack), you may discard a Fire Energy attached to this Pokémon. If you do, switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Inferno Onrush',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
