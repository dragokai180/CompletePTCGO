from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='05f28044-85e6-5e62-9730-2be421d1ab58',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name',
    display_name='Bibarel',
    searchable_by=['Bibarel', 'Stage 1', 'Bibarel'],
    subtypes=['Stage 1'],
    collector_number=172,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name',
    family_id=399,
    abilities=[
        Ability(
            title='Unaware',
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pokémon.",
            passive=standard_passive("Prevent all effects of your opponent's attacks, except damage, done to this Pokémon."),
        ),
        Attack(
            title='Amnesia',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
            locks_next_turn=False,
        ),
    ],
)
