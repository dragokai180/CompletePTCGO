from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8de205ce-7f69-5193-abb9-4747b4aed584',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name',
    display_name='Arcanine',
    searchable_by=['Arcanine', 'Stage 1', 'Arcanine'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    family_id=58,
    abilities=[
        Ability(
            title='Burning Road',
            game_text='Once during your turn (before your attack), if this Pokémon was on the Bench and became your Active Pokémon this turn, you may move any number of Fire Energy attached to your Pokémon to this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Scorching Breath',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
