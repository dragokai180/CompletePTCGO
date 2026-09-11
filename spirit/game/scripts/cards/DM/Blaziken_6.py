from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7ecf6552-197f-5956-af77-1fd0537f0c40',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name',
    display_name='Blaziken',
    searchable_by=['Blaziken', 'Stage 2', 'Blaziken'],
    subtypes=['Stage 2'],
    collector_number=6,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name',
    family_id=255,
    abilities=[
        Ability(
            title='Firestarter',
            game_text='Once during your turn (before your attack), you may attach a Fire Energy card from your discard pile to 1 of your Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Fire Stream',
            game_text="Discard a Fire Energy from this Pokémon. This attack does 20 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
