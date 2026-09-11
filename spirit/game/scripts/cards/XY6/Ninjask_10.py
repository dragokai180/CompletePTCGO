from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c4b1f7d-ec5b-57cb-b8a5-889b665f62c4',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name',
    display_name='Ninjask',
    searchable_by=['Ninjask', 'Stage 1', 'Ninjask'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name',
    family_id=290,
    abilities=[
        Ability(
            title='Wing Buzz',
            game_text="Once during your turn (before your attack), if this Pokémon is your Active Pokémon, you may discard a card from your hand. If you do, discard the top card of your opponent's deck.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Afterimage Assault',
            game_text='Search your deck for up to 2 Ninjask and put them onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
