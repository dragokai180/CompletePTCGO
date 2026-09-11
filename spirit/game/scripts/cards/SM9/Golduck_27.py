from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='51e3e283-ad71-5908-bf1b-c774aad9bd48',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name',
    display_name='Golduck',
    searchable_by=['Golduck', 'Stage 1', 'Golduck'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name',
    family_id=54,
    abilities=[
        Attack(
            title='Amnesia',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Swim',
            game_text="If any of your opponent's Pokémon have any Water Energy attached to them, you may do 90 damage to 1 of your opponent's Benched Pokémon instead of their Active Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
