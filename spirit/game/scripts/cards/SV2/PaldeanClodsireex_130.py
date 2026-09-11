from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fa59bde5-c882-5eee-82b5-b06b88a7a116',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsireex.Name',
    display_name='Paldean Clodsire ex',
    searchable_by=['Paldean Clodsire ex', 'Stage 1', 'ex', 'PaldeanClodsireex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=130,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name',
    family_id=194,
    abilities=[
        Ability(
            title='Toxic Wetland',
            game_text="Once during your turn, if a Stadium is in play, you may make your opponent's Active Pokémon Poisoned.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Needle Bone',
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
