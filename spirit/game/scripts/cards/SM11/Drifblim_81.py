from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c03ef5b-4271-52d5-b88f-c13dc134530c',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name',
    display_name='Drifblim',
    searchable_by=['Drifblim', 'Stage 1', 'Drifblim'],
    subtypes=['Stage 1'],
    collector_number=81,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    family_id=425,
    abilities=[
        Ability(
            title='Tag Transport',
            game_text='Once during your turn (before your attack), you may switch your Active TAG TEAM Pokémon with 1 of your Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
