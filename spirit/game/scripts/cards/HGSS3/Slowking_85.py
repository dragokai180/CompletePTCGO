from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dc6547d0-0e4e-558b-a03e-5f528a14b1f3',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name',
    display_name='Slowking',
    searchable_by=['Slowking', 'Stage 1', 'Prime', 'Slowking'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=85,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=79,
    abilities=[
        Ability(
            title="Opponent's Choice",
            game_text="Once during your turn (before your attack), you may reveal the top 2 cards of your deck and your opponent chooses 1 of them. Put that card into your hand and the other card on the bottom of your deck. This power can't be used if Slowking is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Super Psy Bolt',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
